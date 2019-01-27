import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomepageComponent } from './homepage/homepage.component';
import { TriviaComponent } from './trivia/trivia.component';

const routes: Routes = [
  {path: '', component: HomepageComponent},
  {path: 'trivia', component: TriviaComponent}
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }
