import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GrammarCheckService2 {
  private apiUrl = 'https://ai-based-spelling-and-grammar-correction.p.rapidapi.com/data';
  private apiKey = 'd673b331acmsh29fca2d1fa03c58p18a7aejsn8822f575c2c0';

  constructor(private http: HttpClient) { }

  checkGrammar(textToCheck: string): Observable<string> {
    const headers = new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded',
      'X-RapidAPI-Key': this.apiKey,
      'X-RapidAPI-Host': 'ai-based-spelling-and-grammar-correction.p.rapidapi.com'
    });

    const body = new URLSearchParams({
      text: textToCheck
    });

    return this.http.post(this.apiUrl, body.toString(), { headers, responseType: 'text' });
  }
}
