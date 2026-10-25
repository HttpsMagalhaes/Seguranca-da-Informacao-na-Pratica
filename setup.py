import time
import sys

def carregar_etapa(mensagem, tempo=5):
    print(f"🔄 {mensagem}...")
    time.sleep(tempo)

print("="*60)
print("⚙️  Iniciando configuração do ambiente Gemini Lab...")
print("="*60)
time.sleep(1)

carregar_etapa("Conectando aos servidores do Google")
carregar_etapa("Baixando pacotes de Inteligência Artificial (gemini-core)")
carregar_etapa("Instalando dependências de visão computacional")
carregar_etapa("Concedendo permissões de administrador ao script")

print("\n" + "!"*60)
print("🚨 VOCÊ CAIU NO GOLPE DO COMANDO CEGO! 🚨")
print("!"*60 + "\n")

time.sleep(1)
print("Regra de Cibersegurança para Devs: NUNCA rode um script da internet sem ler o código-fonte antes.")
print("\nSe este arquivo fosse um Cavalo de Troia (Trojan) real, neste exato momento o invasor poderia ter:")
print(" ❌ Roubado todas as senhas salvas no seu navegador.")
print(" ❌ Copiado suas chaves SSH e credenciais do GitHub.")
print(" ❌ Instalado um Keylogger invisível na sua máquina.")
print("\nO GitHub hospeda o código, mas não garante a sua segurança.")
print("A pressa e a confiança cega são as maiores vulnerabilidades de um sistema.")
