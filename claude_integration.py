#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de Integração com Claude API para PROT-Relatório-Automático
Automação completa: análise de fotos → extração de dados → geração de relatórios
"""

import os
import base64
import json
import re
from datetime import datetime
from typing import Dict, List, Optional
import anthropic

class ProtClaudeIntegration:
      """Integração com Claude para processamento automático de relatórios PROT"""

    def __init__(self, api_key: Optional[str] = None):
              """Inicializa cliente Claude"""
              self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
              if not self.api_key:
                            raise ValueError("ANTHROPIC_API_KEY não configurada. Configure em .env ou como variável de ambiente")

              self.client = anthropic.Anthropic(api_key=self.api_key)
              self.model = "claude-3-5-sonnet-20241022"

    def encode_image_to_base64(self, image_path: str) -> str:
              """Converte imagem para base64"""
              with open(image_path, "rb") as image_file:
                            return base64.standard_b64encode(image_file.read()).decode("utf-8")

          def analyze_label_image(self, image_path: str) -> Dict:
                    """
                            Analisa imagem de rótulo e extrai dados de proteína

                                            Retorna:
                                                    {
                                                                "tipo": "Paleta sem pele",
                                                                            "peso_kg": 702.89,
                                                                                        "lote": "ABC123",
                                                                                                    "data_fabricacao": "2026-07-01",
                                                                                                                "data_validade": "2026-09-30",
                                                                                                                            "confianca": 95,
                                                                                                                                        "notas": "..."
                    }
                            """
                    try:
                                  image_data = self.encode_image_to_base64(image_path)

            prompt = """Você é um especialista em leitura de rótulos de proteína animal. 
            Analise esta imagem de rótulo e extraia EXATAMENTE as seguintes informações:

            1. TIPO DE PROTEÍNA (ex: Paleta sem pele, Bisteca, Calabresa, etc)
            2. PESO/QUANTIDADE em kg
            3. NÚMERO DE LOTE
            4. DATA DE FABRICAÇÃO (formato DD/MM/YYYY)
            5. DATA DE VALIDADE (formato DD/MM/YYYY)

            IMPORTANTE: Retorne APENAS um JSON válido, sem explicações, no seguinte formato:
            {
                "tipo": "...",
                    "peso_kg": ...,
                        "lote": "...",
                            "data_fabricacao": "DD/MM/YYYY",
                                "data_validade": "DD/MM/YYYY",
                                    "confianca": 0-100,
                                        "notas": "..."
}

Se não conseguir ler algum campo, coloque null e explique em "notas"."""

            response = self.client.messages.create(
                              model=self.model,
                              max_tokens=500,
                              messages=[
                                                    {
                                                                              "role": "user",
                                                                              "content": [
                                                                                                            {
                                                                                                                                              "type": "image",
                                                                                                                                              "source": {
                                                                                                                                                                                    "type": "base64",
                                                                                                                                                                                    "media_type": "image/jpeg",
                                                                                                                                                                                    "data": image_data,
                                                                                                                                                },
                                                                                                              },
                                                                                                            {
                                                                                                                                              "type": "text",
                                                                                                                                              "text": prompt
                                                                                                              }
                                                                                ],
                                                    }
                              ],
            )

            # Parse JSON response
            response_text = response.content[0].text
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)

            if json_match:
                              data = json.loads(json_match.group())
                              # Converter datas para formato ISO
                              if data.get("data_fabricacao"):
                                                    data["data_fabricacao"] = self._convert_date_to_iso(data["data_fabricacao"])
                                                if data.get("data_validade"):
                                                                      data["data_validade"] = self._convert_date_to_iso(data["data_validade"])
                                                                  return data

            return {"erro": "Não consegui extrair dados do rótulo", "confianca": 0}

except Exception as e:
            return {"erro": f"Erro ao analisar imagem: {str(e)}", "confianca": 0}

    def analyze_nf_image(self, image_path: str) -> Dict:
              """
                      Analisa imagem de NF-e e extrai dados

                                      Retorna:
                                              {
                                                          "numero": "268969",
                                                                      "serie": "1",
                                                                                  "emissor": "Dom Porquito Agroindustrial S.A.",
                                                                                              "data": "2026-07-02",
                                                                                                          "valor": 43235.63,
                                                                                                                      "confianca": 95
                                                                                                                              }
                                                                                                                                      """
              try:
                            image_data = self.encode_image_to_base64(image_path)

            prompt = """Você é um especialista em leitura de Notas Fiscais Eletrônicas (NF-e).
            Analise esta imagem de NF-e e extraia EXATAMENTE:

            1. NÚMERO DA NF-e
            2. SÉRIE
            3. NOME/RAZÃO SOCIAL DO EMISSOR
            4. DATA DE EMISSÃO (DD/MM/YYYY)
            5. VALOR TOTAL DA NOTA

            Retorne APENAS um JSON válido:
            {
                "numero": "...",
                    "serie": "...",
                        "emissor": "...",
                            "data": "DD/MM/YYYY",
                                "valor": ...,
                                    "confianca": 0-100
                                    }"""

            response = self.client.messages.create(
                              model=self.model,
                              max_tokens=500,
                              messages=[
                                                    {
                                                                              "role": "user",
                                                                              "content": [
                                                                                                            {
                                                                                                                                              "type": "image",
                                                                                                                                              "source": {
                                                                                                                                                                                    "type": "base64",
                                                                                                                                                                                    "media_type": "image/jpeg",
                                                                                                                                                                                    "data": image_data,
                                                                                                                                                },
                                                                                                              },
                                                                                                            {
                                                                                                                                              "type": "text",
                                                                                                                                              "text": prompt
                                                                                                              }
                                                                                ],
                                                    }
                              ],
            )

            response_text = response.content[0].text
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)

            if json_match:
                              data = json.loads(json_match.group())
                              if data.get("data"):
                                                    data["data"] = self._convert_date_to_iso(data["data"])
                                                return data

            return {"erro": "Não consegui extrair dados da NF-e", "confianca": 0}

except Exception as e:
            return {"erro": f"Erro ao analisar NF-e: {str(e)}", "confianca": 0}

    def gerar_relatorio_completo(self, nf_data: Dict, proteinas: List[Dict], observacoes: str = "") -> str:
              """
                      Claude gera relatório em formato Markdown
                              """
        prompt = f"""Você é um especialista em relatórios de qualidade de entrega de proteína animal.
        Gere um relatório profissional PROT com os seguintes dados:

        NF-e: {nf_data['numero']}.{nf_data['serie']}
        Emissor: {nf_data['emissor']}
        Data: {nf_data['data']}
        Valor: R$ {nf_data['valor']}

        PROTEÍNAS ENTREGUES:
        {json.dumps(proteinas, indent=2, ensure_ascii=False)}

        Observações adicionais: {observacoes}

        Gere um relatório em Markdown bem estruturado com:
        - Título
        - Dados da NF-e
        - Tabela de proteínas
        - Análise de conformidade
        - Alertas (se houver)
        - Conclusão e recomendações"""

        response = self.client.messages.create(
                      model=self.model,
                      max_tokens=2000,
                      messages=[
                                        {
                                                              "role": "user",
                                                              "content": prompt
                                        }
                      ]
        )

        return response.content[0].text

    def processar_entrega_completa(self, nf_image_path: str, label_images: List[str], data_entrega: str) -> Dict:
              """
                      Processamento 100% automático:
                              1. Lê NF-e
                                      2. Lê rótulos
                                              3. Gera relatório
                                                      4. Retorna dados estruturados
                                                              """
        resultado = {
                      "status": "processando",
                      "nf_data": None,
                      "proteinas": [],
                      "relatorio": None,
                      "erros": []
        }

        # Processar NF-e
        print("📄 Analisando NF-e...")
        nf_data = self.analyze_nf_image(nf_image_path)
        if "erro" in nf_data:
                      resultado["erros"].append(f"Erro na NF-e: {nf_data['erro']}")
else:
            resultado["nf_data"] = nf_data

        # Processar rótulos
        print("🏷️ Analisando rótulos...")
        for idx, label_path in enumerate(label_images, 1):
                      print(f"  Rótulo {idx}/{len(label_images)}...")
            proteina = self.analyze_label_image(label_path)
            if "erro" not in proteina:
                              resultado["proteinas"].append(proteina)
else:
                resultado["erros"].append(f"Erro no rótulo {idx}: {proteina['erro']}")

        # Gerar relatório
        if resultado["nf_data"] and resultado["proteinas"]:
                      print("📝 Gerando relatório...")
            resultado["relatorio"] = self.gerar_relatorio_completo(
                              resultado["nf_data"],
                              resultado["proteinas"],
                              ""
            )

        resultado["status"] = "concluído"
        resultado["data_processamento"] = datetime.now().isoformat()
        return resultado

    @staticmethod
    def _convert_date_to_iso(date_str: str) -> str:
              """Converte DD/MM/YYYY para YYYY-MM-DD"""
        try:
                      if len(date_str) == 10 and date_str[2] == "/" and date_str[5] == "/":
                                        day, month, year = date_str.split("/")
                                        return f"{year}-{month}-{day}"
                                except:
            pass
        return date_str


# Exemplo de uso
if __name__ == "__main__":
      # Para testar, você precisa:
      # 1. Definir ANTHROPIC_API_KEY como variável de ambiente
      # 2. Ter imagens de teste em ./test_images/

    print("🤖 PROT-Relatório-Automático com Claude Integration")
    print("=" * 60)

    try:
              integration = ProtClaudeIntegration()
        print("✅ Conexão com Claude estabelecida")
        print(f"   Modelo: {integration.model}")
        print("\n💡 Para usar:")
        print("   1. Importe ProtClaudeIntegration")
        print("   2. Chame analyze_label_image() ou analyze_nf_image()")
        print("   3. Use processar_entrega_completa() para automação total")

except ValueError as e:
        print(f"❌ Erro: {e}")
