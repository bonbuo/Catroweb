<?php

namespace App\Project\CatrobatCode\Statements;

class HideTextStatement extends Statement
{
  /**
   * @var string
   */
  final public const BEGIN_STRING = 'hide variable ';
  /**
   * @var string
   */
  final public const END_STRING = ')<br/>';

  public function __construct(mixed $statementFactory, mixed $xmlTree, mixed $spaces)
  {
    parent::__construct($statementFactory, $xmlTree, $spaces,
      self::BEGIN_STRING,
      self::END_STRING);
  }

  public function getBrickText(): string
  {
    $variable_name = $this->xmlTree->userVariableName;

    return 'Hide variable '.$variable_name;
  }

  public function getBrickColor(): string
  {
    return '1h_brick_red.png';
  }
}
