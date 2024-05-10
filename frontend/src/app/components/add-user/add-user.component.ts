import { Component } from '@angular/core';
import { User } from '../../models/user.model';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-add-user',
  templateUrl: './add-user.component.html',
  styleUrls: ['./add-user.component.css'],
})
export class AddUserComponent {
  user: User = {
    user_id: crypto.randomUUID(),
    user_name: '',
    age: '',
    address: ""
  };
  submitted = false;

  constructor(private userService: UserService) {}

  saveUser(): void {
    const data = {
      user_id: this.user.user_id,
      user_name: this.user.user_name,
      age: this.user.age,
      address: this.user.address
    };

    this.userService.create(data).subscribe({
      next: (res) => {
        console.log(res);
        this.submitted = true;
      },
      error: (e) => console.error(e)
    });
  }

  newUser(): void {
    this.submitted = false;
    this.user = {
      user_id: crypto.randomUUID(),
      user_name: '',
      age: '',
      address: ""
    };
  }
}
