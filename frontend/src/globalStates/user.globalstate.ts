import { BehaviorSubject, Observable } from 'rxjs'
import { UserModel } from '@models/user.model'
import { Injectable } from '@angular/core'

@Injectable({
    providedIn: 'root',
})
export class UserGlobalState {
    private readonly userSubject: BehaviorSubject<UserModel | null> = new BehaviorSubject<UserModel | null>(null)

    // Observable público para que los componentes puedan suscribirse
    public user$: Observable<UserModel | null> = this.userSubject.asObservable()

    // Getter para obtener el valor actual del usuario
    get currentUser(): UserModel | null {
        return this.userSubject.getValue()
    }

    // Setter para actualizar el usuario
    setUser(user: UserModel | null): void {
        this.userSubject.next(user)
    }
}
