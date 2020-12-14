import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';

export interface dataStructure {
  meta?: any;
  items: any[];
}

@Injectable({
  providedIn: 'root'
})
export class CurriculumService {

  constructor(private http: HttpClient) { }

  public getAssets(baseURL) {
    return this.http.get(baseURL + 'api/v2/assets/?format=json');
  };

  public getPrograms(baseURL) {
    return this.http.get(baseURL + 'api/v2/programs/?format=json');
  };

  public getAudiences(baseURL) {
    return this.http.get(baseURL + 'api/v2/audiences/?format=json');
  };

  public getLearningSpaces(baseURL) {
    console.log('learning Spaces: ', baseURL + 'api/v2/learning-spaces/?format=json')
    return this.http.get(baseURL + 'api/v2/learning-spaces/?format=json');
  };

  public getTopics(baseURL) {
    return this.http.get(baseURL + 'api/v2/topics/?format=json');
  };

  public getTags(baseURL) {
    return this.http.get(baseURL + 'api/v2/tags/?format=json');
  };

  public getAssetTypes(baseURL) {
    return this.http.get(baseURL + 'api/v2/asset-type/?format=json');
  };

  public getActivityTypes(baseURL) {
    return this.http.get(baseURL + 'api/v2/activity-type/?format=json');
  };

  public getModules(baseURL) {
    return this.http.get(baseURL + 'api/v2/modules/?format=json');
  };

  public getLessons(baseURL) {
    return this.http.get(baseURL + 'api/v2/lessons/?format=json');
  };

  public getActivities(baseURL) {
    return this.http.get(baseURL + 'api/v2/activities/?format=json');
  };

}
