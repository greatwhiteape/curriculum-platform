import { Component, ElementRef, ViewEncapsulation } from '@angular/core';
import { faPlus, faMinus } from '@fortawesome/free-solid-svg-icons';
import { CurriculumService, dataStructure } from './curriculum.service';
import { ProgramsPipe } from './programs.pipe';
import { TagPipe } from './tag.pipe';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  providers: [ProgramsPipe, TagPipe],
  encapsulation: ViewEncapsulation.None,
  styles: [`
    .card.disabled {
      opacity: 0.5;
    }
  `]
})

export class AppComponent {
  // Search tags toggle
  disabled = false;
  active = 1;

  programsIcon = this.disabled ? 'faMinus' : 'faPlus';
  faPlus = faPlus;
  faMinus = faMinus;

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
  asset_types;
  selected_asset_types;
  selected_asset_types_count: number = 0;
  activity_types;
  selected_activity_types;
  selected_activity_types_count: number = 0;
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

  modulesOnly: boolean = true;   // Original
  // modulesOnly: boolean = false; // TROUBLESHOOTING

  constructor(private elm: ElementRef, private currService: CurriculumService) {
    this.modulesOnly = (elm.nativeElement.getAttribute('modulesOnly')) ? elm.nativeElement.getAttribute('modulesOnly') : false;

    this.currService.getTags(this.baseURL).subscribe((data: dataStructure) => {
      this.tags = data.items;
      console.log('Tags: ', this.tags);
      this.tags.forEach(element => {
        element.selected = (element.tag === elm.nativeElement.getAttribute('tag')) ? true : false;
      });
      this.getSelectedTags();
    });

    this.currService.getPrograms(this.baseURL).subscribe((data: dataStructure) => {
      this.programs = data.items;
      console.log('Programs: ', this.programs);
      this.programs.forEach(element => {
        element.selected = (element.program_name === elm.nativeElement.getAttribute('program')) ? true : false;
      });
    });

    this.currService.getAudiences(this.baseURL).subscribe((data: dataStructure) => {
      this.audiences = data.items;
      console.log('Audience: ', this.audiences);
      this.audiences.forEach(element => {
        element.selected = false;
      });
    });

    this.currService.getTopics(this.baseURL).subscribe((data: dataStructure) => {
      this.topics = data.items;
      console.log('Topics: ', this.topics);
      this.topics.forEach(element => {
        element.selected = false;
      });
    });

    this.currService.getActivityTypes(this.baseURL).subscribe((data: dataStructure) => {
      this.activity_types = data.items;
      console.log('Activity Type: ', this.activity_types);
      this.activity_types.forEach(element => {
        element.selected = false;
      });
    });

    this.currService.getAssetTypes(this.baseURL).subscribe((data: dataStructure) => {
      this.asset_types = data.items;
      console.log('Asset Type: ', this.asset_types);
      this.asset_types.forEach(element => {
        element.selected = false;
      });
    });

    this.currService.getModules(this.baseURL).subscribe((data: dataStructure) => {
      // this.modules = data.items;
      this.modules = [];
      data.items.forEach(module => {
        (module.live) ? this.modules.push(module) : null ;
      })
      console.log('Modules: ', this.modules);
      this.modules.forEach(element => {
        element.selected = false;
      });
      this.getSelectedPrograms();
    });

    this.currService.getLessons(this.baseURL).subscribe((data: dataStructure) => {
      this.lessons = [];
      data.items.forEach(lesson => {
        (lesson.live) ? this.lessons.push(lesson) : null ;
      })
      console.log('Lessons: ', this.lessons);
      this.lessons.forEach(element => {
        element.selected = false;
      });
      this.getSelectedPrograms();
    });

    this.currService.getAssets(this.baseURL).subscribe((data: dataStructure) => {
      this.assets = [];
      data.items.forEach(asset => {
        (asset.live) ? this.assets.push(asset) : null ;
      })
      console.log('Assets: ', this.assets);
      this.assets.forEach(element => {
        element.selected = false;
      });
      this.getSelectedPrograms();
    });

    this.currService.getActivities(this.baseURL).subscribe((data: dataStructure) => {
      this.activities = [];
      data.items.forEach(activity => {
        activity.live ? this.activities.push(activity) : null ;
      })
      console.log('Activities: ', this.activities);
      this.activities.forEach(element => {
        element.selected = false;
      });
      this.getSelectedPrograms();
    });


    // this.currService.getAssets(this.baseURL).subscribe((response: CustomResponse) => {
    //   if (response) {
    //     const data: any = Object.entries(response);
    //     console.log('Get Assets: ',data);
    //     if (data[0][1]) {
    //       console.log(data[0][1])
    //       data.forEach(array => {
    //         array[1].forEach(element => {
    //           this.assets.push(element);
    //         });
    //       });
    //     }
    //   }
    // });


    // this.currService.getActivities(this.baseURL).subscribe((response: CustomResponse) => {
    //   if (response) {
    //     const data: any = Object.entries(response);
    //     console.log(data);
    //     if (data[0][1]) {
    //       console.log(data[0][1])
    //       data.forEach(array => {
    //         console.log(array);
    //         array[1].forEach(element => {
    //           console.log(element, this.activities)
    //           this.activities.push(element);
    //           console.log(this.activities)
    //         });
    //       });
    //     }
    //   }
    // });

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
    console.log('Get Selected Tags: ',this.selected_tags, this.tags);
    this.selected_tags = this.tags.filter(s => {
      return s.selected;
    });
  }

  getSelectedTopics() {
    this.selected_topics = this.topics.filter(s => {
      return s.selected;
    });
  }

  getSelectedActivityTypes() {
    this.selected_activity_types = this.activity_types.filter(s => {
      return s.selected;
    });
  }

  getSelectedAssetTypes() {
    this.selected_asset_types = this.asset_types.filter(s => {
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
    this.getSelectedActivityTypes();
    this.getSelectedAssetTypes();
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
  deleteActivityType(id: number) {
    this.activity_types = this.activity_types.filter(g => {
      if (g.id == id) {
        g.selected = false;
      }
      return true;
    });
    this.getSelectedActivityTypes();
  }

  // Delete Single Listed program Tag
  deleteAssetType(id: number) {
    this.asset_types = this.asset_types.filter(g => {
      if (g.id == id) {
        g.selected = false;
      }
      return true;
    });
    this.getSelectedAssetTypes();
  }
}

export interface CustomResponse {
  data: any;
}
