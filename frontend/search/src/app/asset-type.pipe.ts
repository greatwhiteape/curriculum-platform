import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'assetType'
})
export class AssetTypePipe implements PipeTransform {
  transform(items: any[], selected_types?: any[]): any[] {
    if (!items) { return [{}]; }
    if (!selected_types) { return items; }
    console.log('Asset Type Pipe: ', items, selected_types);
    return items.filter( item => this.checkFilter(item, selected_types));
  }

  checkFilter(object, selected_types) {
    if (selected_types.length > 0) {
      const some = selected_types.some(type => object.asset_type.id === type.id);
      console.log('Asset Type Pipe checkFilter: ', some);
      return some;
    } else {
      return true;
    }
  }

}
