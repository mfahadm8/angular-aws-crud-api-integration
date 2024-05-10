import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { User } from '../models/user.model';

const baseUrl = 'https://jb35ecbie4.execute-api.us-east-1.amazonaws.com/prod/user';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  constructor(private http: HttpClient) {}

  getAll(): Observable<User[]> {
    return this.http.get<User[]>(baseUrl);
  }

  get(id: any): Observable<User> {
    return this.http.get<User>(`${baseUrl}?user_id=${id}`);
  }

  create(data: any): Observable<any> {
    return this.http.post(baseUrl, data);
  }

  update( data: any): Observable<any> {
    return this.http.post(baseUrl, data);
  }

  findByTitle(name: any): Observable<User[]> {
    return this.http.get<User[]>(`${baseUrl}?name=${name}`);
  }
}
