<?php

namespace App\Project\CatrobatCode\Parser\Bricks;

use App\Project\CatrobatCode\Parser\Constants;

class TurnLeftBrick extends Brick
{
  protected function create(): void
  {
    $this->type = Constants::TURN_LEFT_BRICK;
    $this->caption = 'Turn left _ degrees';
    $this->setImgFile(Constants::MOTION_BRICK_IMG);
  }
}
