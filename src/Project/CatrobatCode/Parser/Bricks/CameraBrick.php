<?php

namespace App\Project\CatrobatCode\Parser\Bricks;

use App\Project\CatrobatCode\Parser\Constants;

class CameraBrick extends Brick
{
  protected function create(): void
  {
    $this->type = Constants::CAMERA_BRICK;
    $this->caption = 'Turn camera _';
    $this->setImgFile(Constants::LOOKS_BRICK_IMG);
  }
}
