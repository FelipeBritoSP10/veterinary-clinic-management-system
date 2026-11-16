"""
Módulo Principal de Execução (CLI Terminal)
Permite cadastrar animais, veterinários, equipamentos, e gerar prontuários com exames.
"""
from models import Veterinario, Animal, Equipamento, ExameLaboratorial, ExameImagem, Prontuario
from repository import ClinicaRepository


def executar_cenario_demonstracao(repo: ClinicaRepository):
    print("\n=======================================================")
    print("   EXECUÇÃO DO CENÁRIO DE TESTE - CLÍNICA VETERINÁRIA  ")
    print("=======================================================")
    
    vet = Veterinario(nome="Dra. Camila Souza", telefone="91 98877-6655", crmv="PA-12345", especialidade="Cirurgia & Diagnóstico")
    ultrasound = Equipamento(nome="Aparelho de Ultrassom Portátil", status_operacional="Operacional / Calibrado")
    
    repo.adicionar_veterinario(vet)
    repo.adicionar_equipamento(ultrasound)
    
    paciente = Animal(nome="Thor", especie="Canino (Golden Retriever)", idade=4)
    repo.adicionar_animal(paciente)
    
    print(f"\n1. ATENDIMENTO INICIAL:")
    print(f"   {vet.realizar_atendimento(paciente)}")
    print(f"   {ultrasound.verificar_status()}")
    
    prontuario = Prontuario(codigo="PRON-2026-001", animal=paciente, veterinario=vet)
    
    exame_sangue = ExameLaboratorial(descricao="Hemograma Completo com Plaquetas", valor_base=80.0, taxa_reagente=25.0)
    exame_raio_x = ExameImagem(descricao="Raio-X Torácico Digital", valor_base=150.0, taxa_equipamento=45.0)
    
    prontuario.adicionar_exame(exame_sangue)
    prontuario.adicionar_exame(exame_raio_x)
    repo.adicionar_prontuario(prontuario)
    
    print(f"\n2. EXECUÇÃO POLIMÓRFICA DOS EXAMES E CÁLCULO DE CUSTOS:")
    custo_total = prontuario.calcular_custo_total()
    
    print(f"\n3. RESUMO DO PRONTUÁRIO:")
    print(f"   Código Prontuário : {prontuario.codigo}")
    print(f"   Paciente           : {prontuario.animal.get_info()}")
    print(f"   Veterinário Resp.  : {prontuario.veterinario.nome} (CRMV: {prontuario.veterinario.crmv})")
    print(f"   ---------------------------------------------------")
    print(f"   CUSTO TOTAL DO ATENDIMENTO: R$ {custo_total:.2f}")
    print("=======================================================\n")


def menu_interativo():
    repo = ClinicaRepository()
    
    # Cadastros iniciais de exemplo
    repo.adicionar_veterinario(Veterinario("Dr. Felipe Brito", "91 8178-4689", "PA-9988", "Clínica Geral"))
    repo.adicionar_equipamento(Equipamento("Raio-X Digital", "Operacional"))
    repo.adicionar_animal(Animal("Mel", "Felino", 2))

    while True:
        print("\n==================================================")
        print("   SISTEMA DE GERENCIAMENTO DE CLÍNICA VETERINÁRIA")
        print("==================================================")
        print("1. Cadastrar Novo Animal (Paciente)")
        print("2. Cadastrar Novo Veterinário")
        print("3. Cadastrar Novo Equipamento")
        print("4. Criar Prontuário e Executar Exames (Cenário)")
        print("5. Listar Cadastros (Animais, Veterinários, Equipamentos)")
        print("6. Executar Cenário Automático de Avaliação")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            print("\n--- CADASTRO DE ANIMAL ---")
            nome = input("Nome do animal: ").strip()
            especie = input("Espécie (ex: Canino, Felino): ").strip()
            try:
                idade = int(input("Idade: ").strip())
                animal = Animal(nome, especie, idade)
                repo.adicionar_animal(animal)
                print(f"Sucesso: Animal '{nome}' cadastrado com sucesso!")
            except ValueError:
                print("Erro: A idade deve ser um número inteiro.")
                
        elif opcao == "2":
            print("\n--- CADASTRO DE VETERINÁRIO ---")
            nome = input("Nome do veterinário: ").strip()
            telefone = input("Telefone: ").strip()
            crmv = input("CRMV (ex: PA-12345): ").strip()
            especialidade = input("Especialidade: ").strip()
            try:
                vet = Veterinario(nome, telefone, crmv, especialidade)
                repo.adicionar_veterinario(vet)
                print(f"Sucesso: Veterinário(a) '{nome}' cadastrado(a) com sucesso!")
            except ValueError as e:
                print(f"Erro no cadastro: {e}")
                
        elif opcao == "3":
            print("\n--- CADASTRO DE EQUIPAMENTO ---")
            nome = input("Nome do equipamento: ").strip()
            status = input("Status operacional (ex: Operacional, Manutenção): ").strip()
            eq = Equipamento(nome, status)
            repo.adicionar_equipamento(eq)
            print(f"Sucesso: Equipamento '{nome}' cadastrado!")
            
        elif opcao == "4":
            print("\n--- CRIAR PRONTUÁRIO E EXECUTAR EXAMES ---")
            if not repo.animais:
                print("Erro: Cadastre pelo menos um animal primeiro (Opção 1).")
                continue
            if not repo.veterinarios:
                print("Erro: Cadastre pelo menos um veterinário primeiro (Opção 2).")
                continue
            
            print("\nAnimais disponíveis:")
            for i, a in enumerate(repo.animais):
                print(f"[{i}] {a.get_info()}")
            idx_a = int(input("Escolha o número do animal: "))
            
            print("\nVeterinários disponíveis:")
            for i, v in enumerate(repo.veterinarios):
                print(f"[{i}] Dr(a). {v.nome} (CRMV: {v.crmv})")
            idx_v = int(input("Escolha o número do veterinário: "))
            
            codigo_prontuario = input("Código do Prontuário (ex: PRON-100): ").strip()
            
            prontuario = Prontuario(codigo=codigo_prontuario, animal=repo.animais[idx_a], veterinario=repo.veterinarios[idx_v])
            
            while True:
                print("\nAdicionar Exame:")
                print("1. Exame Laboratorial (com reagente)")
                print("2. Exame de Imagem (com equipamento)")
                print("0. Finalizar prontuário")
                t_exame = input("Escolha: ").strip()
                
                if t_exame == "1":
                    desc = input("Descrição do exame laboratorial: ").strip()
                    v_base = float(input("Valor base (R$): "))
                    t_reag = float(input("Taxa de reagente (R$): "))
                    prontuario.adicionar_exame(ExameLaboratorial(desc, v_base, t_reag))
                elif t_exame == "2":
                    desc = input("Descrição do exame de imagem: ").strip()
                    v_base = float(input("Valor base (R$): "))
                    t_eq = float(input("Taxa de equipamento (R$): "))
                    prontuario.adicionar_exame(ExameImagem(desc, v_base, t_eq))
                elif t_exame == "0":
                    break
            
            repo.adicionar_prontuario(prontuario)
            print(f"\nProntuário {prontuario.codigo} criado com sucesso!")
            total = prontuario.calcular_custo_total()
            print(f"VALOR TOTAL DOS EXAMES: R$ {total:.2f}")
            
        elif opcao == "5":
            print("\n--- LISTA DE CADASTROS ---")
            print(f"-> Veterinários ({len(repo.veterinarios)}):")
            for v in repo.veterinarios:
                print(f"   • {v.nome} | CRMV: {v.crmv} | {v.especialidade}")
            print(f"-> Animais ({len(repo.animais)}):")
            for a in repo.animais:
                print(f"   • {a.get_info()}")
            print(f"-> Equipamentos ({len(repo.equipamentos)}):")
            for e in repo.equipamentos:
                print(f"   • {e.verificar_status()}")
            print(f"-> Prontuários Registrados ({len(repo.prontuarios)})")
            
        elif opcao == "6":
            executar_cenario_demonstracao(repo)
            
        elif opcao == "0":
            print("\nEncerrando sistema... Até logo!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    menu_interativo()
