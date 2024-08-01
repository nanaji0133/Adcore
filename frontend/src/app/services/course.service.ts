import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CourseService {
  private apiUrl = 'http://127.0.0.1:5000/api/courses'; // Use IPv4

  async getCourses(search: string = ''): Promise<any[]> {
    const url = `${this.apiUrl}?search=${encodeURIComponent(search)}`;
    const response = await fetch(url);
    return response.json();
  }

  async getCourse(id: string): Promise<any> {
    const response = await fetch(`${this.apiUrl}/${id}`);
    return response.json();
  }

  async createCourse(course: any): Promise<any> {
    const response = await fetch(this.apiUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(course)
    });
    return response.json();
  }

  async updateCourse(id: string, course: any): Promise<any> {
    const response = await fetch(`${this.apiUrl}/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(course)
    });
    return response.json();
  }

  async deleteCourse(id: string): Promise<void> {
    await fetch(`${this.apiUrl}/${id}`, {
      method: 'DELETE'
    });
  }
}
