import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { FontAwesomeModule } from '@fortawesome/angular-fontawesome'

import { AppComponent } from './app.component';
import { SafePipe } from './safe.pipe';
import { AudiencesPipe } from './audiences.pipe';
import { ProgramsPipe } from './programs.pipe';
import { TopicPipe } from './topic.pipe';
import { TagPipe } from './tag.pipe';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { AssetTypePipe } from './asset-type.pipe';
import { ActivityTypePipe } from './activity-type.pipe';
import { LearningSpacePipe } from './learning-space.pipe';

@NgModule({
   declarations: [
      AppComponent,
      SafePipe,
      AudiencesPipe,
      ProgramsPipe,
      TopicPipe,
      TagPipe,
      AssetTypePipe,
      ActivityTypePipe,
      LearningSpacePipe,
      LearningSpacePipe,
   ],
   imports: [
      BrowserModule,
      HttpClientModule,
      FormsModule,
      NgbModule,
      FontAwesomeModule
   ],
   providers: [],
   bootstrap: [
      AppComponent
   ]
})
export class AppModule { }
