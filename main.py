import flet as ft

def main(page=ft.Page):
    # Configuração inicial do título
    title = ft.Text("Lohan Chat 😎", size=30)
    page.add(title)

    # Função para abrir o popup de entrada no chat
    def abrir_popup(event):
        popup.open = True
        page.update()

    # Função para enviar mensagem pelo túnel de comunicação
    def send_message_tunnel(message):
        chat.controls.append(ft.Text(message))  # Adiciona a mensagem ao chat
        page.update()

    # Inscrição no túnel de comunicação
    page.pubsub.subscribe(send_message_tunnel)

    # Função para enviar uma mensagem no chat
    def send_message(event):
        text_message = box_message.value  # Obtém o texto da mensagem
        name = box_name.value  # Obtém o nome do usuário
        message = f"{name}: {text_message}"  # Formata a mensagem
        page.pubsub.send_all(message)  # Envia para todos os inscritos
        box_message.value = ""  # Limpa o campo de mensagem
        page.update()

    # Caixa de texto para mensagem e botão de envio
    box_message = ft.TextField(label="Digite a mensagem", on_submit=send_message)
    button_message = ft.ElevatedButton("Send", on_click=send_message)
    row_msg = ft.Row([box_message, button_message])  # Organiza mensagem e botão em uma linha

    # Área onde as mensagens aparecerão
    chat = ft.Column()

    # Função para entrar no chat após preencher o nome
    def enter_chat(event):
        popup.open = False  # Fecha o popup
        page.remove(title)  # Remove o título inicial
        page.remove(button)  # Remove o botão inicial
        page.add(chat)  # Adiciona o espaço do chat
        page.add(row_msg)  # Adiciona o campo de mensagem e botão de envio
        name = box_name.value
        message = f"{name} entrou no chat"
        page.pubsub.send_all(message)  # Notifica a entrada do usuário
        page.update()

    # Botão inicial para abrir o popup de entrada no chat
    button = ft.ElevatedButton("Join Chat", on_click=abrir_popup, width=150, height=40, style=ft.ButtonStyle(text_style=ft.TextStyle(size=18)))
    page.add(button)

    # Configuração do popup para entrada no chat
    title_popup = ft.Text("Welcome to the chat")  # Título do popup
    box_name = ft.TextField(label="Enter your name")  # Campo para o nome do usuário
    button_go_chat = ft.ElevatedButton("To enter", on_click=enter_chat)  # Botão para confirmar entrada
    popup = ft.AlertDialog(title=title_popup, content=box_name, actions=[button_go_chat])  # Popup completo
    page.dialog = popup

# Inicializa o app no navegador
ft.app(main, view=ft.WEB_BROWSER)
