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
  private currentQ: String = 'YEET';
  private url = 'http://127.0.0.1:5000/trivia/';

  constructor(private http: HttpClient, private service: TopicService) { }

  ngOnInit() {
    this.http.get(this.url + this.service.getTopic()).subscribe(
      (res: any) => {
        console.log(res);
        this.questions = res[0];
        this.answers = res[1];
      }
    );
  }

  onEnter(ans: String) {
    //
    console.log('HELLO');
  }
}
