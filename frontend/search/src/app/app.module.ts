import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { SafePipe } from './safe.pipe';
import { AudiencesPipe } from './audiences.pipe';
import { ProgramsPipe } from './programs.pipe';
import { TopicPipe } from './topic.pipe';
import { TagPipe } from './tag.pipe';
import { TypePipe } from './type.pipe';

@NgModule({
  declarations: [
    AppComponent,
    SafePipe,
    AudiencesPipe,
    ProgramsPipe,
    TopicPipe,
    TagPipe,
    TypePipe
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
