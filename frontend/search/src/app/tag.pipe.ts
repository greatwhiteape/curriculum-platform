import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'tag'
})
export class TagPipe implements PipeTransform {
  transform(items: any[], selected_tags: any[]): any[] {
    if (!items) { return [{}]; }
    if (!selected_tags) { return items; }
    return items.filter( item => this.checkFilter(item, selected_tags));
  }

  checkFilter(object, selected_tags) {
    if (selected_tags.length > 0) {
      const some = selected_tags.some(tag => object.tag_relationship.some(item => item.tag.id === tag.id));
      return some;
    } else {
      return true;
    }
  }
}
