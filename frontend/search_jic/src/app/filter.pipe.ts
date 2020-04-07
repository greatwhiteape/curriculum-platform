import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'programFilter'
})
export class ProgramFilterPipe implements PipeTransform {
  transform(items: any[], selected_programs?: any[]): any[] {
    console.log('Filter: ', this, this.checkFilter);
    if (!items) { return [{}]; }
    if (!selected_programs) { return items; }

    return items.filter( item => this.checkFilter(item, selected_programs));
  }

  checkFilter(module, selected_programs) {
    if (selected_programs.length > 0) {
      const some = selected_programs.some(program => module.program === program.id);
      return some;
    } else {
      return true;
    }
  }
}

