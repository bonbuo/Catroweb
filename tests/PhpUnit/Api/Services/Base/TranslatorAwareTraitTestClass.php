<?php

namespace Tests\PhpUnit\Api\Services\Base;

use App\Api\Services\Base\TranslatorAwareInterface;
use App\Api\Services\Base\TranslatorAwareTrait;

class TranslatorAwareTraitTestClass implements TranslatorAwareInterface
{
  use TranslatorAwareTrait;
}
