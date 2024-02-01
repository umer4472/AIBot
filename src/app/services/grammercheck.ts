import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GrammarCheckService {
  apiUrl = 'https://grammar-and-spellcheck.p.rapidapi.com/grammarandspellcheck';
  apiKey = 'd673b331acmsh29fca2d1fa03c58p18a7aejsn8822f575c2c0';

  constructor(private http: HttpClient) {}

  checkGrammar(text: string): Observable<any> {
    const headers = new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded',
      'X-RapidAPI-Key': this.apiKey,
      'X-RapidAPI-Host': 'grammar-and-spellcheck.p.rapidapi.com'
    });

    const body = new URLSearchParams({
      query: text
    });

    return this.http.post(this.apiUrl, body.toString(), { headers });
  }
}
