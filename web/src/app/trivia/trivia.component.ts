import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { TopicService } from '../topic.service';

@Component({
  selector: 'app-trivia',
  templateUrl: './trivia.component.html',
  styleUrls: ['./trivia.component.css']
})
export class TriviaComponent implements OnInit {
  private questions: String[];
  private answers: String[];
  private currentQ: String = 'No questions found';
  private url = 'http://127.0.0.1:5000/trivia/';

  constructor(private http: HttpClient, private service: TopicService) { }

  ngOnInit() {
    this.http.get(this.url + this.service.getTopic()).subscribe(
      (res: any) => {
        console.log(res);
        if (res[0].length !== -1) {
          this.questions = res[0];
          this.currentQ = this.questions[0];
          this.answers = res[1];
        }
      }
    );
  }

  onEnter(ans: String) {
    if (this.answers.indexOf(ans) !== -1) {
      console.log('ya');
      if (this.questions.length !== 0) {
        this.questions = this.questions.slice(0);
        this.currentQ = this.questions[0];
      } else {
        this.currentQ = 'No more questions';
      }
    }
  }
}
