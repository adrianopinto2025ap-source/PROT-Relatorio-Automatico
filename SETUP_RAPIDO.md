# ⚡ SETUP RÁPIDO - PROT em 5 Minutos

## 🚀 Como Rodar AGORA (sem gerar API Key)

### **Passo 1: Clone o Repositório**
```bash
git clone https://github.com/adrianopinto2025ap-source/PROT-Relatorio-Automatico.git
cd PROT-Relatorio-Automatico
```

### **Passo 2: Instale as Dependências**
```bash
pip install -r requirements.txt
```

### **Passo 3: Configure o .env (TESTE)**
Crie um arquivo `.env` na raiz do projeto:

```bash
# Modo de teste (sem precisar de API Key)
FLASK_ENV=development
FLASK_DEBUG=true
ANTHROPIC_API_KEY=test-key-123  # Apenas para teste

# Banco de dados
DATABASE_PATH=prot_database.db

# Upload
UPLOAD_FOLDER=uploads
MAX_UPLOAD_SIZE=16777216
```

### **Passo 4: Execute o Servidor**
```bash
python app.py
```

Você verá algo como:
```
 * Running on http://0.0.0.0:5000
 * Press CTRL+C to quit
```

### **Passo 5: Acesse no Navegador**
Abra seu navegador e vá para:
```
http://localhost:5000
```

✅ **Pronto! Sistema rodando!**

---

## 📝 O que Você Pode Fazer Agora

1. ✅ Preencher formulários com dados de NF-e
2. 2. ✅ Adicionar proteínas manualmente
   3. 3. ✅ Gerar relatórios PDF/DOCX
      4. 4. ✅ Ver dados armazenados no banco
         5. 5. ✅ Testar a interface web
           
            6. ---
           
            7. ## 🔑 Quando Tiver sua API Key do Claude
           
            8. 1. Vá para `https://platform.claude.com/settings/keys`
               2. 2. Crie uma chave API (sk-ant-...)
                  3. 3. No arquivo `.env`, substitua:
                     4.    ```
                              ANTHROPIC_API_KEY=sk-ant-sua-chave-aqui
                              ```
                           4. Reinicie o servidor (`python app.py`)
                           5. 5. Agora você pode:
                              6.    - ✅ Fazer upload de fotos
                                    -    - ✅ Claude lerá automaticamente
                                         -    - ✅ Gerar relatórios automaticamente
                                          
                                              - ---

                                              ## 🆘 Problemas Comuns

                                              ### "ModuleNotFoundError: No module named 'flask'"
                                              ```bash
                                              # Solução: instale as dependências
                                              pip install -r requirements.txt
                                              ```

                                              ### "Port 5000 already in use"
                                              ```bash
                                              # Solução: use outra porta
                                              python -c "from app import app; app.run(port=5001)"
                                              ```

                                              ### "Permission denied" no Windows
                                              ```bash
                                              # Solução: use Python diretamente
                                              python app.py
                                              ```

                                              ### Banco de dados vazio
                                              - É normal! Ao enviar dados pelo formulário, eles serão salvos
                                              - - Verifique a pasta `uploads/` para arquivos gerados
                                               
                                                - ---

                                                ## 📱 Interface Web

                                                Ao acessar `http://localhost:5000`, você verá:

                                                - **Formulário de Entrega**: Preencha dados manualmente
                                                -   - Número PROT
                                                    -   - Data da entrega
                                                        -   - Dados da NF-e
                                                            -   - Proteínas entregues
                                                             
                                                                - - **Botão Gerar Relatório**: Cria PDF + DOCX automaticamente
                                                                 
                                                                  - - **Lista de Relatórios**: Visualize todas as entregas processadas
                                                                   
                                                                    - ---

                                                                    ## 🔗 Próximos Passos

                                                                    1. **Testar com dados exemplo** - Use os dados de exemplo abaixo:
                                                                    2.    ```
                                                                             PROT: PROT-002/2026
                                                                             Data: 2026-07-09
                                                                             NF-e: 268969.1
                                                                             Emissor: Dom Porquito
                                                                             Valor: R$ 43.235,63

                                                                             Proteína 1:
                                                                             - Tipo: Paleta sem pele
                                                                             - Peso: 702.89 kg
                                                                             - Lote: ABC123
                                                                             - Validade: 30/09/2026
                                                                             ```

                                                                          2. **Gerar sua API Key** quando quiser automação completa
                                                                      
                                                                          3. 3. **Usar com Claude** para ler fotos automaticamente
                                                                            
                                                                             4. ---
                                                                            
                                                                             5. ## 📚 Documentação Completa
                                                                            
                                                                             6. - `README.md` - Visão geral e features
                                                                                - - `GUIA_CLAUDE.md` - Guia completo com Claude
                                                                                  - - `.env.example` - Todas as configurações disponíveis
                                                                                   
                                                                                    - ---

                                                                                    ## 💬 Dúvidas?

                                                                                    Se algo não funcionar:
                                                                                    1. Verifique a pasta `uploads/` foi criada
                                                                                    2. 2. Veja se a porta 5000 está livre
                                                                                       3. 3. Confira se Python 3.8+ está instalado
                                                                                          4. 4. Leia `GUIA_CLAUDE.md` para mais detalhes
                                                                                            
                                                                                             5. ---
                                                                                            
                                                                                             6. **Status:** ✅ Pronto para usar | **Tempo:** ~5 minutos | **Custo:** Grátis (por enquanto)
