import { Component, ElementRef } from '@angular/core';
import { CurriculumService } from './curriculum.service';
import { ProgramsPipe } from './programs.pipe';
import { TagPipe } from './tag.pipe';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  providers: [ProgramsPipe, TagPipe]
})

export class AppComponent {


  title = 'Search';
  baseURL = 'https://teach.gmri.org/'
  // baseURL = 'http://localhost/'

  programs;
  selected_programs;
  selected_program_count: number = 0;
  audiences;
  selected_audiences;
  selected_audience_count: number = 0 ;
  tags;
  selected_tags;
  selected_tags_count: number = 0;
  topics;
  selected_topics;
  selected_topics_count: number = 0;
  types;
  selected_types;
  selected_types_count: number = 0;
  modules;
  selected_modules;
  selected_module_count: number = 0;
  lessons;
  selected_lessons;
  selected_lesson_count: number = 0;

  activities = [];
  selected_activities;
  selected_activities_count: number = 0;

  assets = [];
  selected_assets;
  selected_asset_count: number = 0;

  modulesOnly: boolean = true;
  
  constructor(private elm: ElementRef, private currService: CurriculumService) {
    this.modulesOnly = (elm.nativeElement.getAttribute('modulesOnly')) ? elm.nativeElement.getAttribute('modulesOnly') : false;

    this.currService.getTags(this.baseURL).subscribe((data) => {
      this.tags = data;
      this.tags.forEach(element => {
        element.selected = (element.tag === elm.nativeElement.getAttribute('tag')) ? true : false;
      });
      this.getSelectedTags();
    });

    this.currService.getPrograms(this.baseURL).subscribe((data) => {
      this.programs = data;
      this.programs.forEach(element => {
        element.selected = (element.program_name === elm.nativeElement.getAttribute('program')) ? true : false;
      });
    });

    this.currService.getAudiences(this.baseURL).subscribe((data) => {
      this.audiences = data;
      this.audiences.forEach(element => {
        element.selected = false;
      });
    });

    this.currService.getTopics(this.baseURL).subscribe((data) => {
      this.topics = data;
      this.topics.forEach(element => {
        element.selected = false;
      });
    });

    this.currService.getTypes(this.baseURL).subscribe((data) => {
      this.types = data;
      this.types.forEach(element => {
        element.selected = false;
      });
    });

    this.currService.getModules(this.baseURL).subscribe((data) => {
      this.modules = data;
      this.modules.forEach(element => {
        element.selected = false;
      });
      this.getSelectedPrograms();
    });

    this.currService.getLessons(this.baseURL).subscribe((data) => {
      this.lessons = data;
      this.lessons.forEach(element => {
        element.selected = false;
      });
      this.getSelectedPrograms();
    });

    this.currService.getAssets(this.baseURL).subscribe((response: CustomResponse) => {
      if (response) {
        const data: any = Object.entries(response);
        console.log(data);
        if (data[0][1]) {
          console.log(data[0][1])
          data.forEach(array => {
            array[1].forEach(element => {
              this.assets.push(element);
            });
          });
        }
      }
    });


    this.currService.getActivities(this.baseURL).subscribe((response: CustomResponse) => {
      if (response) {
        const data: any = Object.entries(response);
        console.log(data);
        if (data[0][1]) {
          console.log(data[0][1])
          data.forEach(array => {
            console.log(array);
            array[1].forEach(element => {
              console.log(element, this.activities)
              this.activities.push(element);
              console.log(this.activities)
            });
          });
        }
      }
    });

  }


  // Getting Selected programs and Count
  getSelectedPrograms() {
    this.selected_programs = this.programs.filter(s => {
      return s.selected;
    });
  }

  // Getting Selected programs and Count
  getSelectedAudiences() {
    this.selected_audiences = this.audiences.filter(s => {
      return s.selected;
    });
  }

  getSelectedTags() {
    this.selected_tags = this.tags.filter(s => {
      return s.selected;
    });
  }

  getSelectedTopics() {
    this.selected_topics = this.topics.filter(s => {
      return s.selected;
    });
  }

  getSelectedTypes() {
    this.selected_types = this.types.filter(s => {
      return s.selected;
    });
  }

  // Clearing All Selections
  clearSelection() {
    this.programs = this.programs.filter(g => {
      g.selected = false;
      return true;
    });
    this.getSelectedPrograms();
    this.getSelectedAudiences();
    this.getSelectedTags();
    this.getSelectedTopics();
    this.getSelectedTypes();
  }

  deleteModulesOnly() {
    this.modulesOnly = false;
    this.getSelectedPrograms;
  }

  // Delete Single Listed program Tag
  deleteProgram(id: number) {
    this.programs = this.programs.filter(g => {
      if (g.id == id) {
        g.selected = false;
      }
      return true;
    });
    this.getSelectedPrograms();
  }

  // Delete Single Listed program Tag
  deleteAudience(id: number) {
    this.audiences = this.audiences.filter(g => {
      if (g.id == id) {
        g.selected = false;
      }
      return true;
    });
    this.getSelectedAudiences();
  }

  // Delete Single Listed program Tag
  deleteTag(id: number) {
    this.tags = this.tags.filter(g => {
      if (g.id == id) {
        g.selected = false;
      }
      return true;
    });
    this.getSelectedTags();
  }

  // Delete Single Listed program Tag
  deleteTopic(id: number) {
    this.topics = this.topics.filter(g => {
      if (g.id == id) {
        g.selected = false;
      }
      return true;
    });
    this.getSelectedTopics();
  }

  // Delete Single Listed program Tag
  deleteType(id: number) {
    this.types = this.types.filter(g => {
      if (g.id == id) {
        g.selected = false;
      }
      return true;
    });
    this.getSelectedTypes();
  }
}

export interface CustomResponse {
  data: any;
}
