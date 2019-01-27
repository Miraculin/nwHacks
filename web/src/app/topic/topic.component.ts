import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-topic',
  templateUrl: './topic.component.html',
  styleUrls: ['./topic.component.css']
})
export class TopicComponent implements OnInit {
  private topic: String;

  constructor(public router: Router) { }

  ngOnInit() {
  }

  onEnter(value: String) {
    this.topic = value;
    this.router.navigate(['/trivia']);
  }
}
