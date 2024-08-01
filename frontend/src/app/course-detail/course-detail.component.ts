import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterModule, Router } from '@angular/router';
import { NgIf } from '@angular/common';
import { CourseService } from '../services/course.service';

@Component({
  selector: 'app-course-detail',
  standalone: true,
  imports: [RouterModule, NgIf],
  templateUrl: './course-detail.component.html',
  styleUrls: ['./course-detail.component.css']
})
export class CourseDetailComponent implements OnInit {
  course: any;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private courseService: CourseService
  ) {}

  async ngOnInit(): Promise<void> {
    const id = this.route.snapshot.paramMap.get('id');
    this.course = await this.courseService.getCourse(id!);
  }

  async deleteCourse(): Promise<void> {
    const id = this.route.snapshot.paramMap.get('id');
    await this.courseService.deleteCourse(id!);
    this.router.navigate(['/courses']);
  }
}
