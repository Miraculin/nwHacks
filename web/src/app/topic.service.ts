import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TopicService {
  private topic: String = '';

  constructor() { }

  setTopic(str: String) {
    this.topic = str;
  }

  getTopic() {
    return this.topic;
  }
}
