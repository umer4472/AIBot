import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { ContactUsComponent } from './contactUs/contactUs.component';
import { PrivacyPolicyComponent } from './privacyPolicy/privacyPolicy.component';
import { UsecaseModule } from './usecase/usecase.module';
import { RouterModule } from '@angular/router';


@NgModule({
  declarations: [			
    AppComponent,
      HomeComponent,
      ContactUsComponent,
      PrivacyPolicyComponent
   ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule,
    UsecaseModule
  ],
  providers: [
    provideClientHydration()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
