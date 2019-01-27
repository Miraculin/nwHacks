import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-topic',
  templateUrl: './topic.component.html',
  styleUrls: ['./topic.component.css']
})
export class TopicComponent implements OnInit {
  private topic: String;
  private topicButtons: String[];
  private url = 'http://127.0.0.1:5000/categories';

  constructor(
    private router: Router,
    private http: HttpClient) { }

  ngOnInit() {
    this.http.get(this.url).subscribe(
      (res: any) => {
        this.topicButtons = res.map(obj => obj.title).slice(0, 5);
        this.topicButtons = this.topicButtons.map(ele => ele.slice(9));
        console.log(this.topicButtons);
      }
    );
  }

  onClick(elem: any) {
    this.topic = elem.target.textContent;
    console.log(this.topic);
  }

  onEnter(value: String) {
    this.topic = value;
    this.router.navigate(['/trivia']);
  }
}
