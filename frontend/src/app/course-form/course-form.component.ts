import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterModule, Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { NgIf } from '@angular/common';
import { CourseService } from '../services/course.service';

@Component({
  selector: 'app-course-form',
  standalone: true,
  imports: [FormsModule, RouterModule, NgIf],
  templateUrl: './course-form.component.html',
  styleUrls: ['./course-form.component.css']
})
export class CourseFormComponent implements OnInit {
  course: any = {};

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private courseService: CourseService
  ) {}

  async ngOnInit(): Promise<void> {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.course = await this.courseService.getCourse(id);
    }
  }

  async saveCourse(): Promise<void> {
    if (this.course._id) {
      await this.courseService.updateCourse(this.course._id, this.course);
    } else {
      await this.courseService.createCourse(this.course);
    }
    this.router.navigate(['/courses']);
  }
}
