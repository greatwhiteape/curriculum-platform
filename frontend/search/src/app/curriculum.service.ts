import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CurriculumService {

  constructor(private http: HttpClient) { }

  public getAssets(baseURL) {
    console.log('Assets: ', baseURL + 'curriculum/assets/')
    return this.http.get(baseURL + 'curriculum/assets/');
  }

  public getPrograms(baseURL) {
    return this.http.get(baseURL + 'curriculum/taxa/program/');
  }

  public getAudiences(baseURL) {
    return this.http.get(baseURL + 'curriculum/taxa/audience/');
  }

  public getTopics(baseURL) {
    return this.http.get(baseURL + 'curriculum/taxa/topic/');
  }

  public getTags(baseURL) {
    return this.http.get(baseURL + 'curriculum/taxa/tag/');
  }

  public getTypes(baseURL) {
    return this.http.get(baseURL + 'curriculum/taxa/type/');
  }

  public getModules(baseURL) {
    console.log('getModules: ', baseURL + 'curriculum/modules/');
    return this.http.get(baseURL + 'curriculum/modules/');
  }

  public getLessons(baseURL) {
    console.log('getLessons: ', baseURL + 'curriculum/lessons/');
    return this.http.get(baseURL + 'curriculum/lessons/');
  }

  public getActivities(baseURL) {
    console.log('getActivities: ', baseURL + 'curriculum/activities/');
    return this.http.get(baseURL + 'curriculum/activities/');
  }

}
