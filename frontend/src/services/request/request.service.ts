import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http'
import { environment } from '@environments/environment'
import { Injectable } from '@angular/core'
import { Observable } from 'rxjs'

@Injectable({
    providedIn: 'root',
})
export class RequestService {
    private readonly baseUrl = environment.apiUrl

    constructor(private readonly http: HttpClient) {}

    get<T>(endpoint: string, params?: HttpParams, headers?: HttpHeaders): Observable<T> {
        const options = { params, headers }
        return this.http.get<T>(`${this.baseUrl}${endpoint}`, options)
    }

    post<T>(endpoint: string, body: any, headers?: HttpHeaders): Observable<T> {
        return this.http.post<T>(`${this.baseUrl}${endpoint}`, body, { headers })
    }

    put<T>(endpoint: string, body: any, headers?: HttpHeaders): Observable<T> {
        return this.http.put<T>(`${this.baseUrl}${endpoint}`, body, { headers })
    }

    delete<T>(endpoint: string, headers?: HttpHeaders): Observable<T> {
        return this.http.delete<T>(`${this.baseUrl}${endpoint}`, { headers })
    }
}
