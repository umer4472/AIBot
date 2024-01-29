import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-chatBot',
  templateUrl: './chatBot.component.html',
  styleUrls: ['./chatBot.component.css']
})
export class ChatBotComponent implements OnInit {
  messages: string[] = [];

  sendMessage(message: string) {
    this.messages.push(message);
  }

  constructor() { }

  ngOnInit() {
  }

}
