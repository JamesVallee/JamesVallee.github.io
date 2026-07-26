---
layout: default
permalink: /experience/
title: Work Experience
nav: experience
banner_image: /assets/images/Experience-Banner.jpg
subtitle: Applied engineering experience across industry and research.
page_theme: experience
---

<section class="featured-projects full-width">
  <div class="page-content">
    <h2>Professional Experience</h2>
    <div class="project-grid">
      {% assign sorted_experience = site.experience | sort: "end_date" | reverse %}
      {% for job in sorted_experience %}
        <a href="{{ job.url }}"
           class="project-item"
           style="background-image: url('{{ job.banner_image }}');">
          <div class="overlay">
            <div class="overlay-content">
              <h3>{{ job.title }}</h3>
              <span class="project-tag">{{ job.company }}</span>
            </div>
          </div>
        </a>
      {% endfor %}
    </div>
  </div>
</section>
