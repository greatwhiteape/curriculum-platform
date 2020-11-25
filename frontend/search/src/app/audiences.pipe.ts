import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'audiences'
})
export class AudiencesPipe implements PipeTransform {
  transform(items: any[], selected_audiences?: any[]): any[] {
    if (!items) { return [{}]; }
    if (!selected_audiences) { return items; }
    console.log('Audience Filter: ', items, selected_audiences);
    return items.filter( item => this.checkFilter(item, selected_audiences));
  }

  checkFilter(object, selected_audiences) {
    if (selected_audiences.length > 0) {
      console.log('Selected Audiences: ',selected_audiences);
      console.log('Object: ', object);
      const some = selected_audiences.some(audience => object.audience_relationship.some(item => item.audience.id === audience.id));
      // const some = selected_audiences.some(audience => object.audience)
      return some;
    } else {
      return true;
    }
  }
}
