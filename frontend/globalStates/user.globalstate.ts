import { BehaviorSubject, Observable } from 'rxjs'
import { Injectable } from '@angular/core'
import { User } from '@models/user.model'

@Injectable({
    providedIn: 'root',
})
export class UserGlobalState {
    private readonly userSubject: BehaviorSubject<User | null> = new BehaviorSubject<User | null>(null)

    // Observable público para que los componentes puedan suscribirse
    public user$: Observable<User | null> = this.userSubject.asObservable()

    // Getter para obtener el valor actual del usuario
    get currentUser(): User | null {
        return this.userSubject.getValue()
    }

    // Setter para actualizar el usuario
    setUser(user: User | null): void {
        this.userSubject.next(user)
    }
}
