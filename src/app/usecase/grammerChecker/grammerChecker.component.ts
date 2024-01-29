import { Component, OnInit } from '@angular/core';
import TextGears from 'textgears-api';

@Component({
  selector: 'app-grammerChecker',
  templateUrl: './grammerChecker.component.html',
  styleUrls: ['./grammerChecker.component.css']
})
export class GrammerCheckerComponent implements OnInit {
  textToCheck: string = '';
  wordCount: number = 0;
  maxWords: number = 1000; // Max words limit
  errors: string[] = []; // Initialize errors as an empty array

  constructor() {}

  countWords() {
    if (this.textToCheck.trim().length === 0) {
      // If the text is empty, set the word count to zero
      this.wordCount = 0;
    } else {
      // Otherwise, count the number of words
      this.wordCount = this.textToCheck.trim().split(/\s+/).length;
    }
  }

  onFileSelected(event: any) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = () => {
      this.textToCheck = reader.result as string;
      this.countWords();
    };
    reader.readAsText(file);
  }

  checkGrammar() {
    // Call grammar checking function or API here
    // For demonstration, we'll simulate results with a setTimeout
    setTimeout(() => {
      // Mock results for demonstration purposes
      this.errors = ['This is a grammatical error.', 'Another error here.'];

      // You can replace this with actual grammar check logic
    }, 1000); // Simulate API call delay
  }
  ngOnInit(): void {
      
  }

}
