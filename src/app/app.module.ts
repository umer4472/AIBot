import { NgModule,CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { ContactUsComponent } from './contactUs/contactUs.component';
import { PrivacyPolicyComponent } from './privacyPolicy/privacyPolicy.component';
import { UsecaseModule } from './usecase/usecase.module';
import { RouterModule } from '@angular/router';
import {MatIconModule} from '@angular/material/icon';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'
import { AboutComponent } from './about/about.component';
import { NavbarComponent } from './navbar/navbar.component';
import { FooterComponent } from './footer/footer.component';
import { GrammerCheckerComponent } from './usecase/grammerChecker/grammerChecker.component';
import { PlagiarismCheckerComponent } from './usecase/plagiarismChecker/plagiarismChecker.component';
import { ChatBotComponent } from './usecase/chatBot/chatBot.component';
import { FormsModule } from '@angular/forms';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { QuillModule } from 'ngx-quill';
import { NgxSpinnerModule } from 'ngx-spinner';
import { Router } from '@angular/router';
import { AuthInterceptorService } from './services/authInterception';
import { provideHttpClient, withFetch } from '@angular/common/http';



@NgModule({
  declarations: [						
    AppComponent,
      HomeComponent,
      ContactUsComponent,
      PrivacyPolicyComponent,
      AboutComponent,
      FooterComponent,
      GrammerCheckerComponent,
      PlagiarismCheckerComponent,
      ChatBotComponent,
      NavbarComponent
   ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule,
    UsecaseModule,
    MatIconModule,
    BrowserAnimationsModule,
    FormsModule,HttpClientModule,
    QuillModule.forRoot(),
    NgxSpinnerModule,
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass:AuthInterceptorService,
      multi: true,
      deps: [Router]
    },
    provideHttpClient(withFetch()),
    provideClientHydration()
  ],
  schemas:[CUSTOM_ELEMENTS_SCHEMA] ,
  bootstrap: [AppComponent]
})
export class AppModule { }
