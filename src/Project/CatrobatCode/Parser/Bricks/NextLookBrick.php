<?php

namespace App\Project\CatrobatCode\Parser\Bricks;

use App\Project\CatrobatCode\Parser\Constants;

class NextLookBrick extends Brick
{
  protected function create(): void
  {
    $this->type = Constants::NEXT_LOOK_BRICK;
    $this->caption = 'Next look';
    $this->setImgFile(Constants::LOOKS_BRICK_IMG);
  }
}
