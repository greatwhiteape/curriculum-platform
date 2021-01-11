import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'learningSpace'
})
export class LearningSpacePipe implements PipeTransform {
  transform(items: any[], selected_learning_spaces?: any[]): any[] {
    if (!items) { return [{}]; }
    if (!selected_learning_spaces) { return items; }
    return items.filter( item => this.checkFilter(item, selected_learning_spaces));
  }

  checkFilter(object, selected_learning_spaces) {
    console.log('Object: ', object);
    console.log('Learning Spaces: ', selected_learning_spaces);
    if (selected_learning_spaces.length > 0) {
      const some = selected_learning_spaces.some(learning_space => object.learningspace_relationship.some(item => item.learning_space.id === learning_space.id));
      // const some = selected_learning_spaces.some(learning_space => {
      //   console.log('Learning Space: ', learning_space)
      //   object.learningspace_relationship.some(item => {
      //     console.log('Item: ', item);
      //     item.learning_space.id === learning_space.id;
      //   });
      //   // object.learning_space.id === learning_space.id
      // });
      return some;
    } else {
      return true;
    }
  }
}
