import { Component, OnInit } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { CourseService } from '../services/course.service';
import { NgFor } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-course-list',
  standalone: true,
  templateUrl: './course-list.component.html',
  styleUrls: ['./course-list.component.css'],
  imports: [RouterModule, NgFor, FormsModule, DatePipe]
})
export class CourseListComponent implements OnInit {
  courses: any[] = [];
  search = '';

  constructor(private courseService: CourseService, private router: Router) {}

  async ngOnInit(): Promise<void> {
    this.courses = await this.courseService.getCourses();
  }

  async onSearchChange(): Promise<void> {
    this.courses = await this.courseService.getCourses(this.search);
  }

  async deleteCourse(id: string): Promise<void> {
    await this.courseService.deleteCourse(id);
    this.courses = this.courses.filter(course => course._id !== id);
  }
}
