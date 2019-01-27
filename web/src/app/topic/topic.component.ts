import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { TopicService } from '../topic.service';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json'
  })
};

@Component({
  selector: 'app-topic',
  templateUrl: './topic.component.html',
  styleUrls: ['./topic.component.css']
})
export class TopicComponent implements OnInit {
  private topicButtons: String[];
  private url = 'http://127.0.0.1:5000/';

  constructor(
    private router: Router,
    private http: HttpClient,
    private service: TopicService) { }

  ngOnInit() {
    this.http.get(this.url + 'categories').subscribe(
      (res: any) => {
        this.topicButtons = res.map(obj => obj.title).slice(0, 5);
        this.topicButtons = this.topicButtons.map(ele => ele.slice(9));
        console.log(this.topicButtons);
      }
    );
  }

  onClick(elem: any) {
    this.service.setTopic(elem.target.textContent);
    this.http.put(this.url + 'trivia/' + elem.target.textContent + '/5', elem.target.textContent, httpOptions).subscribe(
      res => {
        console.log(res);
        this.router.navigate(['/trivia']);
      },
      err => {
        console.log('Error occured');
      }
    );

    var x = document.getElementById("scroller");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }

  }

  onEnter(value: String) {
    this.router.navigate(['/trivia']);
  }
}
