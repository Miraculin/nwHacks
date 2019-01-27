import { Component, OnInit, Output } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { TopicService } from '../topic.service';

@Component({
  selector: 'app-trivia',
  templateUrl: './trivia.component.html',
  styleUrls: ['./trivia.component.css']
})
export class TriviaComponent implements OnInit {
  private questions: String[] = [];
  private answers: String[] = [];
  private currentQ: String = 'No questions found';
  private url = 'http://127.0.0.1:5000/trivia/';

  constructor(private http: HttpClient, private service: TopicService) { }

  ngOnInit() {
    this.http.get(this.url + this.service.getTopic()).subscribe(
      (res: any) => {
        console.log(res);
        for (const i of res) {
          if (res.indexOf(i) % 2 === 0) {
            this.questions = this.questions.concat(i);
          } else {
            this.answers = this.answers.concat(i);
          }
        }
        if (this.questions.length !== 0) {
          this.currentQ = this.questions[0];
        }
        console.log(this.questions);
        console.log(this.answers);
      }
    );
  }

  onEnter(ans: String) {
    if (this.answers.indexOf(ans) !== -1) {
      console.log('ya');
      if (this.questions.length !== 0) {
        console.log('aetaewt');
        this.currentQ = this.questions.shift();
      } else {
        this.currentQ = 'No more questions';
      }
    }
  }
}
