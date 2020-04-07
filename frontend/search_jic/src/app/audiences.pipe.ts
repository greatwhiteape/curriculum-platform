import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'audiences'
})
export class AudiencesPipe implements PipeTransform {
  transform(items: any[], selected_audiences?: any[]): any[] {
    if (!items) { return [{}]; }
    if (!selected_audiences) { return items; }

    return items.filter( item => this.checkFilter(item, selected_audiences));
  }

  checkFilter(module, selected_audiences) {
    if (selected_audiences.length > 0) {
      const some = selected_audiences.some(audience => module.audience.some(item => item.id === audience.id));
      return some;
    } else {
      return true;
    }
  }
}
