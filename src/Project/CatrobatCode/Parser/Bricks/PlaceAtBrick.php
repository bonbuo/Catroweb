<?php

namespace App\Project\CatrobatCode\Parser\Bricks;

use App\Project\CatrobatCode\Parser\Constants;

class PlaceAtBrick extends Brick
{
  protected function create(): void
  {
    $this->type = Constants::PLACE_AT_BRICK;
    $this->caption = 'Place at X: _ Y: _';
    $this->setImgFile(Constants::MOTION_BRICK_IMG);
  }
}
