import { Component, OnInit } from '@angular/core';
import { GrammarCheckService } from '../../services/grammercheck';

interface GrammarError {
  category: string;
  context: string;
  errorLength: number;
  message: string;
  offset: number;
  replacements: string[]; // Define replacements property
  ruleId: string;
  ruleIssueType: string;
  sentence: string;
}

@Component({
  selector: 'app-grammerChecker',
  templateUrl: './grammerChecker.component.html',
  styleUrls: ['./grammerChecker.component.css']
})
export class GrammerCheckerComponent implements OnInit {
  textToCheck: string = '';
  wordCount: number = 0;
  maxWords: number = 1000; // Max words limit
  errors: GrammarError[] = []; // Initialize errors as an empty array
  originalText: string = '';

  constructor( private service : GrammarCheckService  ) {}

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

  oncheckGrammar() {
    // Call grammar checking function or API here
    // For demonstration, we'll simulate results with a setTimeout
    setTimeout(() => {
      // Mock results for demonstration purposes
      // this.errors = ['This is a grammatical error.', 'Another error here.'];

      // You can replace this with actual grammar check logic
    }, 1000); // Simulate API call delay
  }
  ngOnInit(): void {
      
  }

  checkGrammar() {
    this.service.checkGrammar(this.textToCheck).subscribe(
      (response: any) => {
        console.log(response);
        if (response && response.identified_mistakes && response.identified_mistakes.length > 0) {
          this.errors = response.identified_mistakes;
        } else {
          this.errors = [];
        }
      },
      (error) => {
        console.error('Error:', error);
      }
    );
  }

  fixError(errorIndex: number) {
    const error = this.errors[errorIndex];
    if (error && error.replacements && error.replacements.length > 0) {
      // Replace error with the first suggestion from replacements array
      this.textToCheck = this.textToCheck.replace(
        error.sentence.substring(error.offset, error.offset + error.errorLength),
        error.replacements[0]
      );
    }
    this.countWords(); // Recalculate word count after fixing error
  }

  resetText() {
    // Reset the input text to its original value
    this.textToCheck = this.originalText;
    this.countWords(); // Recalculate word count after reset
  }

  onSaveOriginalText() {
    // Save the original text before modifications
    this.originalText = this.textToCheck;
  }




  

}
