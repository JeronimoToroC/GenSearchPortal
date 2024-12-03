import { StorageService } from '@services/storage/storage.service'
import { BehaviorSubject, Observable } from 'rxjs'
import { UserModel } from '@models/user.model'
import { Injectable } from '@angular/core'

@Injectable({
    providedIn: 'root',
})
export class UserGlobalState {
    private readonly USER_STORAGE_KEY = 'user'
    private readonly userSubject: BehaviorSubject<UserModel | null>

    public user$: Observable<UserModel | null>

    constructor(private readonly storageService: StorageService) {
        const storedUser = this.storageService.getItem<UserModel>(this.USER_STORAGE_KEY)
        this.userSubject = new BehaviorSubject<UserModel | null>(storedUser)
        this.user$ = this.userSubject.asObservable()
    }

    get currentUser(): UserModel | null {
        return this.userSubject.getValue()
    }

    setUser(user: UserModel | null): void {
        if (user) {
            this.storageService.setItem(this.USER_STORAGE_KEY, user)
        } else {
            this.storageService.removeItem(this.USER_STORAGE_KEY)
        }
        this.userSubject.next(user)
    }
}
