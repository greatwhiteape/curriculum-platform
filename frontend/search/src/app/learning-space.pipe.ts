import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'learning-spaces'
})
export class LearningSpacesPipe implements PipeTransform {
  transform(items: any[], selected_learning_spaces?: any[]): any[] {
    if (!items) { return [{}]; }
    if (!selected_learning_spaces) { return items; }
    return items.filter( item => this.checkFilter(item, selected_learning_spaces));
  }

  checkFilter(object, selected_learning_spaces) {
    if (selected_learning_spaces.length > 0) {
      const some = selected_learning_spaces.some(learning_space => object.learning_space_relationship.some(item => item.learning_space.id === learning_space.id));
      return some;
    } else {
      return true;
    }
  }
}
