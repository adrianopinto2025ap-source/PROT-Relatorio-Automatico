# 🤖 Guia Completo: Integração PROT com Claude

## 🚀 Visão Geral

Este guia mostra como usar a integração completa com Claude API para automação 100% do sistema PROT-Relatório-Automático.

**Com Claude, você consegue:**
- ✅ Fazer upload de fotos de rótulos e NF-e
- - ✅ Claude lê e extrai TODOS os dados automaticamente
  - - ✅ Gera relatórios PDF/DOCX prontos
    - - ✅ Armazena tudo no banco de dados
      - - ⏱️ Tudo acontece em segundos!
       
        - ---

        ## 📋 Pré-requisitos

        ### 1. Chave de API do Claude
        ```bash
        # Obtenha em: https://console.anthropic.com/
        ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxxxxx
        ```

        ### 2. Instalar dependências
        ```bash
        pip install -r requirements.txt
        ```

        ### 3. Configurar variáveis de ambiente
        ```bash
        cp .env.example .env
        # Edite .env e adicione sua API key
        ```

        ---

        ## 💻 Instalação Rápida

        ```bash
        # 1. Clone o repositório
        git clone https://github.com/adrianopinto2025ap-source/PROT-Relatorio-Automatico.git
        cd PROT-Relatorio-Automatico

        # 2. Instale dependências
        pip install -r requirements.txt

        # 3. Configure .env
        cp .env.example .env
        nano .env  # Adicione sua ANTHROPIC_API_KEY

        # 4. Execute
        python app.py

        # 5. Acesse
        # Abra: http://localhost:5000
        ```

        ---

        ## 🔧 Exemplos de Uso

        ### Exemplo 1: Analisar Foto de Rótulo

        ```python
        from claude_integration import ProtClaudeIntegration

        # Inicializar
        integration = ProtClaudeIntegration()

        # Analisar rótulo
        resultado = integration.analyze_label_image("foto_rotulo.jpg")

        print(resultado)
        # Output:
        # {
        #   "tipo": "Paleta sem pele",
        #   "peso_kg": 702.89,
        #   "lote": "ABC123",
        #   "data_fabricacao": "2026-07-01",
        #   "data_validade": "2026-09-30",
        #   "confianca": 98
        # }
        ```

        ### Exemplo 2: Analisar NF-e

        ```python
        # Analisar nota fiscal
        nf = integration.analyze_nf_image("foto_nfe.jpg")

        print(nf)
        # Output:
        # {
        #   "numero": "268969",
        #   "serie": "1",
        #   "emissor": "Dom Porquito Agroindustrial S.A.",
        #   "data": "2026-07-02",
        #   "valor": 43235.63,
        #   "confianca": 99
        # }
        ```

        ### Exemplo 3: Automação Completa

        ```python
        # Processar entrega COMPLETA automaticamente
        resultado = integration.processar_entrega_completa(
            nf_image_path="fotos/nfe_prot002.jpg",
            label_images=[
                "fotos/rotulo_paleta.jpg",
                "fotos/rotulo_bisteca.jpg",
                "fotos/rotulo_calabresa.jpg"
            ],
            data_entrega="2026-07-09"
        )

        # Resultado:
        print(resultado['status'])        # "concluído"
        print(resultado['nf_data'])       # Dados da NF extraídos
        print(resultado['proteinas'])     # Lista de proteínas
        print(resultado['relatorio'])     # Relatório em Markdown
        print(resultado['erros'])         # Qualquer erro encontrado
        ```

        ---

        ## 📡 Endpoints da API

        ### POST /api/analisar-rotulo
        Analisa uma foto de rótulo

        ```bash
        curl -X POST http://localhost:5000/api/analisar-rotulo \
          -F "file=@rotulo.jpg"
        ```

        **Resposta:**
        ```json
        {
          "tipo": "Paleta sem pele",
          "peso_kg": 702.89,
          "lote": "ABC123",
          "data_fabricacao": "2026-07-01",
          "data_validade": "2026-09-30",
          "confianca": 98
        }
        ```

        ### POST /api/analisar-nfe
        Analisa uma foto de NF-e

        ```bash
        curl -X POST http://localhost:5000/api/analisar-nfe \
          -F "file=@nfe.jpg"
        ```

        ### POST /api/processar-entrega-completa
        Automação 100% - processa NF-e + múltiplos rótulos

        ```bash
        curl -X POST http://localhost:5000/api/processar-entrega-completa \
          -F "nf_file=@nfe.jpg" \
          -F "label_files=@rotulo1.jpg" \
          -F "label_files=@rotulo2.jpg" \
          -F "label_files=@rotulo3.jpg" \
          -F "data_entrega=2026-07-09"
        ```

        **Resposta:**
        ```json
        {
          "status": "concluído",
          "nf_data": {...},
          "proteinas": [...],
          "relatorio": "...",
          "erros": [],
          "data_processamento": "2026-07-09T14:30:00"
        }
        ```

        ---

        ## 🎯 Caso de Uso Real: Entrega de Proteínas

        ### Cenário:
        Você recebe uma entrega de proteínas da Dom Porquito Agroindustrial e precisa:
        1. Ler a NF-e
        2. 2. Ler os rótulos das 5 proteínas
           3. 3. Gerar relatório PROT
              4. 4. Armazenar tudo
                
                 5. ### Solução com Claude:
                
                 6. ```python
                    from claude_integration import ProtClaudeIntegration
                    from app import db, Entrega

                    # 1. Tirar fotos da entrega
                    # nfe.jpg, paleta.jpg, bisteca.jpg, calabresa.jpg, mascara.jpg, pe.jpg

                    # 2. Processar com Claude
                    integration = ProtClaudeIntegration()
                    resultado = integration.processar_entrega_completa(
                        nf_image_path="nfe.jpg",
                        label_images=[
                            "paleta.jpg",
                            "bisteca.jpg",
                            "calabresa.jpg",
                            "mascara.jpg",
                            "pe.jpg"
                        ],
                        data_entrega="2026-07-09"
                    )

                    # 3. Salvar no banco
                    if resultado['status'] == 'concluído':
                        # Salvar dados extraídos
                        nf = resultado['nf_data']
                        proteinas = resultado['proteinas']

                        # Criar relatório automático
                        relatorio_path = gerar_pdf(nf, proteinas)

                        print(f"✅ Relatório gerado: {relatorio_path}")
                        print(f"📊 Confiança média: {sum([p['confianca'] for p in proteinas]) / len(proteinas)}%")
                    ```

                    ---

                    ## 📊 Resultado Esperado

                    Ao executar a automação completa, você receberá:

                    ```
                    Status: ✅ Concluído

                    NF-e lida:
                      Número: 268969
                      Série: 1
                      Valor: R$ 43.235,63
                      Confiança: 99%

                    Proteínas extraídas: 5
                      1. Paleta sem pele: 702.89 kg | Lote: ABC123 | Validade: 30/09/2026
                      2. Bisteca: 801.28 kg | Lote: DEF456 | Validade: 15/10/2026
                      3. Calabresa: 765 kg | Lote: GHI789 | Validade: 23/09/2026
                      4. Máscara suína: 450 kg | Lote: JKL012 | Validade: 28/11/2026
                      5. Pé suíno: 450 kg | Lote: MNO345 | Validade: 28/09/2026

                    Relatório gerado:
                      📄 PROT-002-2026.pdf
                      📊 PROT-002-2026.docx

                    Tempo total: 8 segundos
                    Custo: ~$0.35
                    ```

                    ---

                    ## 🔍 Verificar Confiança

                    Claude retorna um score de confiança (0-100) para cada leitura:

                    ```python
                    # Score alto = dados foram lidos com certeza
                    if proteina['confianca'] >= 95:
                        print("✅ Dados confiáveis")
                    elif proteina['confianca'] >= 80:
                        print("⚠️  Verificar manualmente")
                    else:
                        print("❌ Baixa confiança - releitura necessária")
                    ```

                    ---

                    ## 💰 Custos da API Claude

                    | Operação | Custo Estimado |
                    |----------|---------------|
                    | Analisar 1 rótulo | ~$0.01 |
                    | Analisar 1 NF-e | ~$0.01 |
                    | Gerar 1 relatório | ~$0.05 |
                    | **Entrega Completa (5 rótulos)** | **~$0.15-0.20** |

                    ---

                    ## 🆘 Troubleshooting

                    ### "ANTHROPIC_API_KEY not found"
                    ```bash
                    # Solução: Configure a variável de ambiente
                    export ANTHROPIC_API_KEY=sk-ant-xxxxx
                    # ou adicione ao .env
                    ```

                    ### "Failed to read image"
                    ```python
                    # Verifique:
                    - Formato suportado: JPG, PNG, GIF
                    - Tamanho máximo: 16MB
                    - Caminho correto do arquivo
                    ```

                    ### "Low confidence score"
                    ```python
                    # Se confiança < 80%:
                    # - Tira foto melhor (melhor iluminação)
                    # - Rótulo legível e sem deformação
                    # - Foto frontal do rótulo
                    ```

                    ---

                    ## 🎓 Dicas Profissionais

                    1. **Melhor foto de rótulo:**
                    2.    - ✅ Bem iluminada
                          -    - ✅ Texto legível
                               -    - ✅ Sem sombras
                                    -    - ✅ Frontal
                                         -    - ❌ Evite ângulos inclinados
                                          
                                              - 2. **Melhor foto de NF-e:**
                                                3.    - ✅ Mostrar número, série, valor, data
                                                      -    - ✅ Boa resolução
                                                           -    - ✅ Sem reflexos
                                                            
                                                                - 3. **Otimizar custos:**
                                                                  4.    - Reutilize dados (não reprocesse a mesma entrega)
                                                                        -    - Batch: processe múltiplas entregas de uma vez
                                                                             -    - Cache: armazene resultados já processados
                                                                              
                                                                                  - ---

                                                                                  ## 📞 Suporte

                                                                                  - Documentação: https://console.anthropic.com/docs
                                                                                  - - GitHub Issues: https://github.com/adrianopinto2025ap-source/PROT-Relatorio-Automatico/issues
                                                                                    - - Email: seu-email@example.com
                                                                                     
                                                                                      - ---

                                                                                      **Status:** ✅ Integração Completa | **Data:** 09/07/2026 | **Versão:** 2.0.0
