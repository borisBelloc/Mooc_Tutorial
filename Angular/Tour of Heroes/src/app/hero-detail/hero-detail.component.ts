import { Component, OnInit, Input } from '@angular/core';
import { Hero } from '../class/hero';
import { HeroService } from '../services/hero.service';

import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';


@Component({
  selector: 'app-hero-detail',
  templateUrl: './hero-detail.component.html',
  styleUrls: ['./hero-detail.component.scss']
})
export class HeroDetailComponent implements OnInit {

  // Allow to pass the hero as :  [hero]="selectedHero" (heroes.component.html)
  @Input() hero: Hero;



  // The ActivatedRoute holds information about the route to this instance of the HeroDetailComponent.
  // This component is interested in the route's parameters extracted from the URL.
  // The "id" parameter is the id of the hero to display.

  // The HeroService gets hero data from the remote server and this component will use it to get the hero-to-display.

  // The location is an Angular service for interacting with the browser.
  // You'll use it later to navigate back to the view that navigated here

  constructor(
    private route: ActivatedRoute,
    private heroService: HeroService,
    private location: Location
  ) { }

  ngOnInit(): void {
    this.getHero();
  }

  getHero(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.heroService.getHero(id)
      .subscribe(hero => this.hero = hero);
  }

}
