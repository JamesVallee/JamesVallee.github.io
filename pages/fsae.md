---
layout: default
title: FSAE Projects
permalink: /fsae/
nav: fsae
banner_image: /assets/images/FSAE/DSC02025.jpg
subtitle: Engineering designs, builds, and racing projects for FSAE competitions.
---

<!-- Projects Grid -->
<section class="featured-projects full-width">
  <div class="page-content">
    <h2>All FSAE Projects</h2>
    <div class="project-grid">
      {% assign sorted_projects = site.fsae | sort: 'title' | reverse %}
      {% for project in sorted_projects %}
        <a href="{{ project.url }}"
           class="project-item"
           style="background-image: url('{{ project.image }}');">
          <div class="overlay">
            <div class="overlay-content">
              <h3>{{ project.title }}</h3>
              <span class="project-tag">FSAE</span>
            </div>
          </div>
        </a>
      {% endfor %}
    </div>
  </div>
</section>
