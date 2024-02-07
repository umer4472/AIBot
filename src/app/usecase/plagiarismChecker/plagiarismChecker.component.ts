import { Component, OnInit } from '@angular/core';
import { PlagiarismCheckerService } from '../../services/plagiarism-checker';
import { NgxSpinnerComponent, NgxSpinnerService } from 'ngx-spinner';

@Component({
  selector: 'app-plagiarismChecker',
  templateUrl: './plagiarismChecker.component.html',
  styleUrls: ['./plagiarismChecker.component.css']
})
export class PlagiarismCheckerComponent implements OnInit {
  textToCheck: string = '';
  wordCount: number = 0;
  maxWords: number = 10000; // Max words limit
  errors: string[] = []; // Initialize errors as an empty array
  plagiarismResult: any = null;

  constructor(private plagiarismCheckerService: PlagiarismCheckerService,  public spinner:NgxSpinnerService) { }

  // Other component methods...

  onFileSelected(event: any) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = () => {
      const fileText = reader.result as string;
      this.textToCheck = fileText; // Set the file text to textToCheck
      this.countWords();
    };
    reader.readAsText(file);
  }

  checkPlagiarism() {
    this.spinner.show();
    this.plagiarismCheckerService.checkPlagiarism(
      this.textToCheck,
      'en', // language
      false, // includeCitations
      false // scrapeSources
    ).subscribe(
      (response) => {
        console.log(response);
        this.plagiarismResult = response; // Store the response in plagiarismResult
        this.spinner.hide();
      },
      (error) => {
        console.error(error);
      }
    );
  }

  countWords() {
    if (this.textToCheck.trim().length === 0) {
      // If the text is empty, set the word count to zero
      this.wordCount = 0;
    } else {
      // Otherwise, count the number of words
      this.wordCount = this.textToCheck.trim().split(/\s+/).length;
    }
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


  ngOnInit() {
  }
}
