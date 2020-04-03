import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'topic'
})
export class TopicPipe implements PipeTransform {
  transform(items: any[], selected_topics?: any[]): any[] {
    if (!items) { return [{}]; }
    if (!selected_topics) { return items; }

    return items.filter( item => this.checkFilter(item, selected_topics));
  }

  checkFilter(object, selected_topics) {
    if (selected_topics.length > 0) {
      const some = selected_topics.some(topics => object.topic.some(item => item.id === topics.id));
      return some;
    } else {
      return true;
    }
  }
}
